"""Exercise protected-main guards in an isolated Git repo; never push anywhere."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


HOOKS = Path(__file__).resolve().parents[1] / '.githooks'


class GitHookTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.repo = Path(cls.temp.name)
        cls.env = os.environ.copy()
        for key in ('GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE'):
            cls.env.pop(key, None)
        cls.env.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM='1')
        cls.git('init', '--initial-branch=main')
        for message in ('first', 'second'):
            cls.git('-c', 'user.name=Hook Test', '-c', 'user.email=hooks@example.invalid',
                    'commit', '--allow-empty', '-m', message)
            setattr(cls, message, cls.git('rev-parse', 'HEAD').stdout.strip())
        cls.git('branch', 'individual/hook-test')
        cls.git('config', 'core.hooksPath', str(HOOKS))

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    @classmethod
    def git(cls, *args, check=True):
        return subprocess.run(['git', *args], cwd=cls.repo, env=cls.env,
                              text=True, capture_output=True, check=check)

    def hook(self, name, *, extra_config=(), allow_push=True, ref=None):
        # Feed hook stdin directly for compatibility with older system Git
        # versions that do not support `git hook run --to-stdin`.
        config = [f'assignment4.allowPush={str(allow_push).lower()}', *extra_config]
        env = self.env.copy()
        env['GIT_CONFIG_COUNT'] = str(len(config))
        for index, item in enumerate(config):
            key, value = item.split('=', 1)
            env[f'GIT_CONFIG_KEY_{index}'] = key
            env[f'GIT_CONFIG_VALUE_{index}'] = value
        return subprocess.run(['sh', str(HOOKS / name)], cwd=self.repo, env=env,
                              input=(ref + '\n') if ref is not None else '',
                              text=True, capture_output=True, check=False)

    def main_update(self, local=None, remote=None):
        return f'refs/heads/main {local or self.second} refs/heads/main {remote or self.first}'

    def personal_update(self):
        return f'refs/heads/individual/test-student {self.second} refs/heads/individual/test-student {self.first}'

    def assert_blocked(self, result, message):
        self.assertNotEqual(result.returncode, 0, result.stderr)
        self.assertIn(message, result.stderr)

    def test_main_commit_is_blocked(self):
        self.assert_blocked(self.hook('pre-commit'), 'Commit blocked')

    def test_personal_branch_commit_is_allowed(self):
        self.git('switch', 'individual/hook-test')
        try:
            result = self.hook('pre-commit')
            self.assertEqual(result.returncode, 0, result.stderr)
        finally:
            self.git('switch', 'main')

    def test_removed_setting_cannot_allow_main_commit(self):
        result = self.hook('pre-commit', extra_config=('assignment4.soloSetup=true',))
        self.assert_blocked(result, 'Commit blocked')

    def test_push_requires_publication_authorization(self):
        result = self.hook('pre-push', allow_push=False, ref=self.personal_update())
        self.assert_blocked(result, 'local-only')

    def test_main_fast_forward_push_is_blocked(self):
        self.assert_blocked(self.hook('pre-push', ref=self.main_update()), 'main is frozen')

    def test_removed_setting_cannot_allow_main_push(self):
        result = self.hook('pre-push', extra_config=('assignment4.soloSetup=true',), ref=self.main_update())
        self.assert_blocked(result, 'main is frozen')

    def test_main_deletion_is_blocked(self):
        result = self.hook('pre-push', ref=self.main_update(local='0' * 40))
        self.assert_blocked(result, 'no direct update or deletion')

    def test_main_history_rewrite_is_blocked(self):
        result = self.hook('pre-push', ref=self.main_update(local=self.first, remote=self.second))
        self.assert_blocked(result, 'no direct update or deletion')

    def test_personal_branch_push_is_allowed(self):
        result = self.hook('pre-push', ref=self.personal_update())
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_main_push_is_blocked_in_a_batch_with_personal_branch(self):
        result = self.hook('pre-push', ref=self.personal_update() + '\n' + self.main_update())
        self.assert_blocked(result, 'main is frozen')


if __name__ == '__main__':
    unittest.main()
