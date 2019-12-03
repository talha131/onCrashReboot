import fs from "fs";
import path from "path";
import { watch, parallel, series } from "gulp";
import { exec } from "child_process";
import { create as browserSyncCreate } from "browser-sync";
const browserSync = browserSyncCreate();

const path404 = path.join(__dirname, "documentation/output/404.html");
const content_404 = () =>
  fs.existsSync(path404) ? fs.readFileSync(path404) : null;

const cleanOutput = () => exec("rm -rf outout/");

const buildContent = () => exec("invoke build");

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
    buildContent
  );
};

const elegant = series(cleanOutput, buildContent, parallel(watchFiles, reload));

exports.elegant = elegant;
exports.default = elegant;
