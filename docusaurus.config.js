// @ts-check

import { themes as prismThemes } from 'prism-react-renderer';

/**
 * @type {import('@docusaurus/types').Config}
 */
export default {
    title: 'Dali Kewara',
    tagline: 'An unexpected journey',
    favicon: 'favicon.ico',

    future: {
        v4: true,
    },

    url: 'https://www.dalikewara.com',
    baseUrl: '/',

    organizationName: 'dalikewara',
    projectName: 'dalikewara.github.io',

    onBrokenLinks: 'throw',
    onBrokenMarkdownLinks: 'warn',

    headTags: [
        {
            tagName: 'link',
            attributes: {
                rel: 'preconnect',
                href: 'https://www.dalikewara.com',
            },
        },
        {
            tagName: 'script',
            attributes: {
                type: 'application/ld+json',
            },
            innerHTML: JSON.stringify({
                '@context': 'https://schema.org/',
                '@type': 'WebSite',
                author:{
                    '@type':"Person",
                    "name":"Dali Kewara",
                    "url":"https://www.dalikewara.com"
                },
                name: 'Dali Kewara',
                url: 'https://www.dalikewara.com',
                logo: 'https://www.dalikewara.com/img/128x128_green_apple.png',
            }),
        },
        {
            tagName: 'link',
            attributes: {
                rel: 'apple-touch-icon',
                sizes: "57x57",
                href: '/favicon/apple-icon-57x57.png',
            },
        },
        {
            tagName: 'link',
            attributes: {
                rel: 'apple-touch-icon',
                sizes: "60x60",
                href: '/favicon/apple-icon-60x60.png',
            },
        },
        {
            tagName: 'link',
            attributes: {
                rel: 'apple-touch-icon',
                sizes: "72x72",
                href: '/favicon/apple-icon-72x72.png',
            },
        },
        {
            tagName: 'link',
            attributes: {
                rel: 'apple-touch-icon',
                sizes: "76x76",
                href: '/favicon/apple-icon-76x76.png',
            },
        },
        {
            tagName: 'link',
            attributes: {
                rel: 'apple-touch-icon',
                sizes: "114x114",
                href: '/favicon/apple-icon-114x114.png',
            },
        },
        {
            tagName: 'link',
            attributes: {
                rel: 'apple-touch-icon',
                sizes: "120x120",
                href: '/favicon/apple-icon-120x120.png',
            },
        },
        {
            tagName: 'link',
            attributes: {
                rel: 'apple-touch-icon',
                sizes: "144x144",
                href: '/favicon/apple-icon-144x144.png',
            },
        },
        {
            tagName: 'link',
            attributes: {
                rel: 'apple-touch-icon',
                sizes: "152x152",
                href: '/favicon/apple-icon-152x152.png',
            },
        },
        {
            tagName: 'link',
            attributes: {
                rel: 'apple-touch-icon',
                sizes: "180x180",
                href: '/favicon/apple-icon-180x180.png',
            },
        },
        {
            tagName: 'link',
            attributes: {
                rel: 'icon',
                type: "image/png",
                sizes: "192x192",
                href: '/favicon/android-icon-192x192.png',
            },
        },
        {
            tagName: 'link',
            attributes: {
                rel: 'icon',
                type: "image/png",
                sizes: "32x32",
                href: '/favicon/favicon-32x32.png',
            },
        },
        {
            tagName: 'link',
            attributes: {
                rel: 'icon',
                type: "image/png",
                sizes: "96x96",
                href: '/favicon/favicon-96x96.png',
            },
        },
        {
            tagName: 'link',
            attributes: {
                rel: 'icon',
                type: "image/png",
                sizes: "16x16",
                href: '/favicon/favicon-16x16.png',
            },
        }
    ],

    i18n: {
        defaultLocale: 'en',
        locales: ['en'],
        localeConfigs: {
            en: {
                label: 'English',
            },
        },
    },

    presets: [
        [
            'classic',
            /**
             * @type {import('@docusaurus/preset-classic').Options}
             */
            (
                {
                    theme: {
                        customCss: [
                            './static/css/color.css',
                            './static/css/navbar.css',
                            './static/css/img.css',
                            './static/css/social.css',
                            './static/css/pagination.css',
                            './static/css/footer.css'
                        ],
                    },
                    docs: {
                        routeBasePath: '/',
                        sidebarPath: './sidebars.js',
                    },
                    blog: false,
                    pages: false,
                    sitemap: {
                        lastmod: 'date',
                        changefreq: 'weekly',
                        priority: 0.5,
                        ignorePatterns: ['/tags/**'],
                        filename: 'sitemap.xml',
                        createSitemapItems: async (params) => {
                            const {defaultCreateSitemapItems, ...rest} = params;
                            const items = await defaultCreateSitemapItems(rest);
                            return items.filter((item) => !item.url.includes('/page/'));
                        },
                    },
                    googleTagManager: {
                        containerId: 'GTM-MMH79W'
                    },
                    gtag: {
                        trackingID: 'G-TBLTVPW7ZD'
                    },
                }
            ),
        ],
    ],

    themeConfig: (
        /**
         * @type {import('@docusaurus/preset-classic').ThemeConfig}
         */
        {
            metadata: [
                {
                    name: 'keywords',
                    content: 'dali, dalikewara, dali kewara, art, writing, journey, coding, code, software engineer, backend developer, backend engineer, programmer, travelling',
                },
                {
                    name: 'google-site-verification',
                    content: 'Czw8BPlbSgfcKuHG56yYHEU2TPLH5TK29b80uJLX-CY',
                },
                {
                    name: 'author',
                    content: 'Dali Kewara',
                },
                {
                    name: 'msapplication-TileImage',
                    content: '/favicon/ms-icon-144x144.png',
                }
            ],
            announcementBar: {
                id: 'work-in-progress',
                content: "🛠 Work In Progress...",
                backgroundColor: 'rgb(0, 0, 0)',
                textColor: 'rgb(225, 225, 225)',
                isCloseable: false,
            },
            colorMode: {
                defaultMode: 'dark',
                disableSwitch: false,
                respectPrefersColorScheme: false,
            },
            navbar: {
                title: 'DK',
                hideOnScroll: true,
                logo: {
                    alt: 'Green Apple Animation Leaf',
                    src: 'img/64x64_green_apple_animation_leaf.gif'
                },
                items: [
                    {
                        type: 'localeDropdown',
                        position: 'right',
                    },
                ],
            },
            footer: {
                copyright: `Copyright © 2017 - ${new Date().getFullYear()} Dali Kewara. All rights reserved. Proudly ❤ made with <a href="https://www.docusaurus.io/" target="_blank" rel="noopener noreferrer">Docusaurus</a>, hosted on <a href="https://www.netlify.com/" target="_blank" rel="noopener noreferrer">Netlify</a> 🚀`,
            },
            prism: {
                theme: prismThemes.github,
                darkTheme: prismThemes.dracula,
            },
        }
    ),
};
