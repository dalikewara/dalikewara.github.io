// @ts-check

import { img } from './img.js';

/**
 * @type {Object}
 */
export const links = {
    // Companies

    vascomm: {
        name: "Vascomm",
        url: "https://www.vascomm.co.id/"
    },
    rctiplus: {
        name: "RCTI+",
        url: "https://www.rctiplus.com/"
    },
    warungpintar: {
        name: "Warung Pintar",
        url: "https://warungpintar.co.id/"
    },
    renos: {
        name: "Renos",
        url: "https://renos.id/"
    },

    // Socials

    instagramprofile: {
        name: "Instagram Profile",
        url: "https://www.instagram.com/dalikewara"
    },
    githubprofile: {
        name: "GitHub Profile",
        url: "https://www.github.com/dalikewara"
    },
    linkedinprofile: {
        name: "LinkedIn Profile",
        url: "https://www.linkedin.com/in/dalikewara"
    },
    freepik: {
        name: "Freepik",
        url: "https://www.flaticon.com/authors/freepik"
    },

    // Repo

    githubrepo: {
        name: "Github",
        url: "https://github.com/dalikewara/dalikewara.github.io"
    },

    // License

    gnugplv3: {
        name: "GNU General Public License v3",
        url: "https://www.gnu.org/licenses/gpl-3.0.en.html"
    },
    gnugplv3faq: {
        name: "https://www.gnu.org/licenses/gpl-faq.html",
        url: "https://www.gnu.org/licenses/gpl-faq.html"
    },

    // Platform

    docusaurus: {
        name: "Docusaurus",
        url: "https://docusaurus.io/",
    },
    flaticon: {
        name: "Flaticon",
        url: "https://www.flaticon.com/"
    },
    netlify: {
        name: "Netlify",
        url: "https://www.netlify.com/",
    },

    // Contents

    solobushcraft: {
        name: "solo bushcraft content",
        url: "https://www.youtube.com/results?search_query=solo+bushcraft+bertram+nagualero"
    },
    charactercodesicons: {
        name: "HTML-CSS-JS",
        url: "https://html-css-js.com/html/character-codes/icons/"
    }
};

/**
 * @param {string} name
 *
 * @returns {JSX.Element}
 */
export function link(name) {
    if (links[name]) {
        return <a href={links[name].url} target="_blank" rel="noopener noreferrer">{links[name].name}</a>
    }
}

/**
 * @param {string} name
 * @param {string} imgName
 *
 * @returns {JSX.Element}
 */
export function linkImg(name, imgName) {
    if (links[name]) {
        return <a href={links[name].url} target="_blank" rel="noopener noreferrer">{img(imgName)}</a>
    }
}
