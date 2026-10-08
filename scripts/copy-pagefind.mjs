// 将 dist/pagefind 复制到 public/pagefind，保证 dev 模式下搜索可用（Windows 兼容版 cp -r）
// 注意：fs.cpSync 在本机 node 上会触发访问违规崩溃（0xC0000005），改用文件级递归复制。
import fs from "node:fs";
import path from "node:path";

const from = "dist/pagefind";
const to = "public/pagefind";

function copyDir(src, dst) {
  fs.mkdirSync(dst, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const s = path.join(src, entry.name);
    const d = path.join(dst, entry.name);
    if (entry.isDirectory()) copyDir(s, d);
    else fs.copyFileSync(s, d);
  }
}

if (fs.existsSync(from)) {
  fs.rmSync(to, { recursive: true, force: true });
  copyDir(from, to);
  console.log("pagefind copied to public/");
} else {
  console.log("dist/pagefind not found, skip");
}
