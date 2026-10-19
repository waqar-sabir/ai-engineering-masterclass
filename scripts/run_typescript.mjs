import { existsSync, readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { spawnSync } from 'node:child_process';

const task = process.argv[2];
if (!['lint', 'test'].includes(task)) throw new Error('Expected lint or test');
const packages = ['projects', 'shared/typescript'].flatMap(root =>
  existsSync(root) ? readdirSync(root, { withFileTypes: true })
    .filter(entry => entry.isDirectory())
    .map(entry => join(root, entry.name))
    .filter(path => existsSync(join(path, 'package.json'))) : []);
if (!packages.length) console.log('No TypeScript packages yet; scaffold check passed.');
for (const path of packages) {
  const pkg = JSON.parse(readFileSync(join(path, 'package.json'), 'utf8'));
  if (!pkg.scripts?.[task]) throw new Error(`${path} must define a ${task} script`);
  const result = spawnSync('npm', ['run', task, '--workspace', path], { stdio: 'inherit' });
  if (result.error) throw result.error;
  if (result.status !== 0) process.exit(result.status ?? 1);
}
