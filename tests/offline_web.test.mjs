import {readFileSync} from 'node:fs';
import {test} from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
const html=readFileSync(new URL('../web/index.html', import.meta.url),'utf8');
const source=html.match(/<script>([\s\S]*?)<\/script>/)?.[1];
assert.ok(source,'inline script present');
const c=vm.createContext({});
vm.runInContext(source.slice(0,source.indexOf('  const $ =')),c);
const calc=(a,b,d)=>vm.runInContext(`calculate(${a},${b},${d})`,c);
test('matches Python calculator defaults and zero percent',()=>{
 assert.deepEqual(JSON.parse(JSON.stringify(calc(200000,35,5000))), {monthly:70000,annual:840000,days:5000/70000*30});
 assert.equal(calc(1000,0,5000).days,null);
});
test('rejects invalid percentages and negative fees',()=>{
 assert.throws(()=>calc(1000,101,0)); assert.throws(()=>calc(1000,40,-10));
});
test('no external runtime resources',()=>{
 assert.doesNotMatch(html,/<script[^>]*src=/i);
 assert.doesNotMatch(html,/<link[^>]*href=/i);
 assert.doesNotMatch(html, /\bfetch\s*\(/);
});
