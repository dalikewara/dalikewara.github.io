import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/__docusaurus/debug',
    component: ComponentCreator('/__docusaurus/debug', '5ff'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/config',
    component: ComponentCreator('/__docusaurus/debug/config', '5ba'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/content',
    component: ComponentCreator('/__docusaurus/debug/content', 'a2b'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/globalData',
    component: ComponentCreator('/__docusaurus/debug/globalData', 'c3c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/metadata',
    component: ComponentCreator('/__docusaurus/debug/metadata', '156'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/registry',
    component: ComponentCreator('/__docusaurus/debug/registry', '88c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/routes',
    component: ComponentCreator('/__docusaurus/debug/routes', '000'),
    exact: true
  },
  {
    path: '/',
    component: ComponentCreator('/', '937'),
    routes: [
      {
        path: '/',
        component: ComponentCreator('/', 'e9a'),
        routes: [
          {
            path: '/',
            component: ComponentCreator('/', '00d'),
            routes: [
              {
                path: '/docs/umar',
                component: ComponentCreator('/docs/umar', '10c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/umar/getting-started',
                component: ComponentCreator('/docs/umar/getting-started', '573'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/umar/what-is',
                component: ComponentCreator('/docs/umar/what-is', '1c0'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/uwais',
                component: ComponentCreator('/docs/uwais', '260'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/uwais/backward-compatibility',
                component: ComponentCreator('/docs/uwais/backward-compatibility', '496'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/uwais/getting-started',
                component: ComponentCreator('/docs/uwais/getting-started', 'aee'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/uwais/project-structure',
                component: ComponentCreator('/docs/uwais/project-structure', '769'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/uwais/what-is',
                component: ComponentCreator('/docs/uwais/what-is', 'fd9'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/ecosystem',
                component: ComponentCreator('/ecosystem', 'd54'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/legal-and-license',
                component: ComponentCreator('/legal-and-license', 'c78'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/',
                component: ComponentCreator('/', 'e09'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
