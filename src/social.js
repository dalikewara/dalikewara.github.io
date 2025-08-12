// @ts-check

import { linkImg } from './link.js';

/**
 * @returns {JSX.Element}
 */
export function social() {
    return <ul className="social">
        <li>
            {linkImg("instagramprofile", "instagram40x40")}
        </li>
        <li>
            {linkImg("githubprofile", "github40x40")}
        </li>
        <li>
            {linkImg("linkedinprofile", "linkedin40x40")}
        </li>
    </ul>
}
