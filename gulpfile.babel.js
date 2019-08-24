import fs from "fs";
import path from "path";
import { watch, parallel } from "gulp";
import { exec } from "child_process";
import { create as browserSyncCreate } from "browser-sync";
const browserSync = browserSyncCreate();

const content_404 = fs.readFileSync(path.join(__dirname, "output/404.html"));

const buildAll = () => exec("invoke build");

const reload = cb => {
  browserSync.init(
    {
      ui: {
        port: 9004
      },
      server: {
        baseDir: "output",
        serveStaticOptions: {
          extensions: ["html"]
        }
      },
      files: "output/*.html",
      port: 9003,
      browser: "google chrome"
    },
    (_, bs) => {
      bs.addMiddleware("*", (_, res) => {
        res.write(content_404);
        res.end();
      });
    }
  );
  cb();
};

const watchFiles = () => {
  watch(
    [
      "content/**/*.md",
      "content/**/*.rest",
      "pelicanconf.py",
      "publishconf.py"
    ],
    { ignoreInitial: false },
    buildAll
  );
};

const elegant = parallel(watchFiles, reload);

exports.elegant = elegant;
exports.default = elegant;
