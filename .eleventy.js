const pluginMinifier = require("@sherby/eleventy-plugin-files-minifier");
const pluginRss = require("@11ty/eleventy-plugin-rss");

module.exports = function(eleventyConfig) {
    eleventyConfig.addPassthroughCopy("assets");
    eleventyConfig.addPassthroughCopy("favicon.ico");
    eleventyConfig.addPassthroughCopy("browserconfig.xml");
    eleventyConfig.addPassthroughCopy("google64385a25e7266f98.html");
    eleventyConfig.addPassthroughCopy("manifest.json");
    eleventyConfig.addPassthroughCopy("robots.txt");
    eleventyConfig.addPlugin(pluginMinifier);
    eleventyConfig.addPlugin(pluginRss);
    eleventyConfig.addPassthroughCopy("post/**/*.png");
    eleventyConfig.addCollection("posts", function (collectionApi) {
        return collectionApi.getFilteredByGlob("post/**/*.md").reverse();
    });
};