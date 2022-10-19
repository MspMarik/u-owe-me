const yaml = require("js-yaml");
const fs = require("node:fs");

function get() {
    let inputfile = "charges.yaml";
    let obj = yaml.load(fs.readFileSync(inputfile, { encoding: "utf-8" }));
    return obj;
}

module.exports = {
    get,
};
