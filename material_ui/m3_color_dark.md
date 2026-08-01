# Material UI

## Color Pairing Rules

Colors must only be used in their intended pairs to ensure accessible contrast:

| Container/Fill        | Text/Icon Color                           |
| --------------------- | ----------------------------------------- |
| `primary`             | `on-primary`                              |
| `primary-container`   | `on-primary-container`                    |
| `secondary`           | `on-secondary`                            |
| `secondary-container` | `on-secondary-container`                  |
| `tertiary`            | `on-tertiary`                             |
| `tertiary-container`  | `on-tertiary-container`                   |
| `error`               | `on-error`                                |
| `error-container`     | `on-error-container`                      |
| `surface`             | `on-surface` or `on-surface-variant`      |
| `surface-container-*` | `on-surface` or `on-surface-variant`      |
| `inverse-surface`     | `inverse-on-surface` or `inverse-primary` |

**Never pair colors outside their intended pairs** — this breaks contrast guarantees, especially under dynamic color and high contrast modes.

## Dark Baseline Colors (Default Contrast)

| Token Name                | Hex Value |
| ------------------------- | --------- |
| Primary Colors            |           |
| primary                   | #D0BCFF   |
| on-primary                | #381E72   |
| primary-container         | #4F378B   |
| on-primary-container      | #EADDFF   |
| Secondary colors          |           |
| secondary                 | #CCC2DC   |
| on-secondary              | #332D41   |
| secondary-container       | #4A4458   |
| on-secondary-container    | #E8DEF8   |
| Tertiary Colors           |           |
| tertiary                  | #EFB8C8   |
| on-tertiary               | #492532   |
| tertiary-container        | #633B48   |
| on-tertiary-container     | #FFD8E4   |
| Error Colors              |           |
| color-error               | #F2B8B5   |
| on-error                  | #601410   |
| error-container           | #8C1D18   |
| on-error-container        | #F9DEDC   |
| Surface Colors            |           |
| surface                   | #141218   |
| on-surface                | #E6E0E9   |
| surface-variant           | #49454F   |
| on-surface-variant        | #CAC4D0   |
| surface-container-highest | #36343B   |
| surface-container-high    | #2B2930   |
| surface-container         | #211F26   |
| surface-container-low     | #1D1B20   |
| surface-container-lowest  | #0F0D13   |
| inverse-surface           | #E6E0E9   |
| inverse-on-surface        | #322F35   |
| surface-tint              | #D0BCFF   |
| surface-tint-color        | #D0BCFF   |
| Outline colors            |           |
| outline                   | #938F99   |
| outline-variant           | #49454F   |
| Addon colors              |           |
| surface-dim               | #141218   |
| surface-bright            | #3B383E   |
| inverse-primary           | #6750A4   |

## Sources

- [M3 Official Site](https://m3.material.io/styles/color/static/baseline)
- [M3 Claude Skill](https://github.com/hamen/material-3-skill)
