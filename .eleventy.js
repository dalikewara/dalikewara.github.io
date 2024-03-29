const pluginMinifier = require("@sherby/eleventy-plugin-files-minifier");
const pluginRss = require("@11ty/eleventy-plugin-rss");

module.exports = function(eleventyConfig) {
    eleventyConfig.addPassthroughCopy("assets");
    eleventyConfig.addPassthroughCopy("favicon.ico");
    eleventyConfig.addPassthroughCopy("browserconfig.xml");
    eleventyConfig.addPassthroughCopy("manifest.json");
    eleventyConfig.addPassthroughCopy("robots.txt");
    eleventyConfig.addPassthroughCopy("post/**/*.png");
    eleventyConfig.addPassthroughCopy("post/**/*.webp");
    eleventyConfig.addPassthroughCopy("post/**/*.jpg");
    eleventyConfig.addCollection("posts", function (collectionApi) {
        return collectionApi.getFilteredByGlob("post/**/*.md").reverse();
    });
    eleventyConfig.addPlugin(pluginMinifier);
    eleventyConfig.addPlugin(pluginRss);
};