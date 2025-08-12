// @ts-check

/**
 * @type {Object}
 */
export const imgs = {
    // Profile

    profilepic: {
        alt: "Profile Picture",
        src: "img/profile-pic.webp"
    },

    // Socials

    instagram20x20: {
        alt: "Instagram",
        src: "img/instagram-20x20.webp"
    },
    instagram40x40: {
        alt: "Instagram",
        src: "img/instagram-40x40.webp"
    },
    github20x20: {
        alt: "GitHub",
        src: "img/github-20x20.webp"
    },
    github40x40: {
        alt: "GitHub",
        src: "img/github-40x40.webp"
    },
    linkedin20x20: {
        alt: "LinkedIn",
        src: "img/linkedin-20x20.webp"
    },
    linkedin40x40: {
        alt: "LinkedIn",
        src: "img/linkedin-40x40.webp"
    },
};

/**
 * @param {string} name
 * @param {string} fragment
 *
 * @returns {JSX.Element}
 */
export function img(name, fragment = '') {
    if (imgs[name]) {
        return <img alt={imgs[name].alt} title={imgs[name].alt} src={imgs[name].src + fragment} />
    }
}
