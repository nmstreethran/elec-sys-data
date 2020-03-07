# ml-elec-model <!-- omit in toc -->

<!-- start badges -->
[![Build Status](https://travis-ci.org/nmstreethran/ml-elec-model.svg?branch=master)](https://travis-ci.org/nmstreethran/ml-elec-model)
[![Code license: MIT](https://img.shields.io/badge/code%20license-MIT-yellow.svg?labelColor=darkslategray)](https://opensource.org/licenses/MIT)
[![Content license: CC BY 4.0](https://img.shields.io/badge/content%20license-CC%20BY%204.0-blue.svg?labelColor=darkslategray)](https://creativecommons.org/licenses/by/4.0/)
[![GitHub Wiki](https://img.shields.io/badge/-GitHub%20Wiki-purple.svg?logo=github&labelColor=black)](https://github.com/nmstreethran/ml-elec-model/wiki)
<!-- end badges -->

by Nithiya Streethran (nmstreethran at gmail dot com)

**This project is a work-in-progress. Feedback and suggestions are always welcome. Please refer to the [contributing guidelines](CONTRIBUTING.md) if you would like to contribute.**

Machine learning-based electricity system model.

## Table of contents <!-- omit in toc -->

- [Requirements](#requirements)
  - [Packages](#packages)
  - [Installation](#installation)
- [Cloning the repository](#cloning-the-repository)
- [Documentation](#documentation)
- [License](#license)
- [Credits](#credits)

## Requirements

### Packages

- [entsoe-py](https://pypi.org/project/entsoe-py/)
- [GeoPandas](https://geopandas.org/)
- [Bokeh](https://bokeh.org/)

### Installation

1. (Recommended) Create and activate a virtual environment:

    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

2. Install dependencies:

    ```sh
    python3 -m pip install entsoe-py geopandas bokeh
    ```

**Using Anaconda:**

1. (Recommended) Create and activate a virtual environment:

    ```sh
    conda create --name ml-elec-model python=3
    conda activate ml-elec-model
    ```

2. Install required packages:

    ```sh
    conda install --channel conda-forge geopandas bokeh
    pip install entsoe-py
    ```

## Cloning the repository

To clone the latest version of this repository, including the contents of the submodule:

**Using HTTPS:**

```sh
git clone --recurse-submodules https://github.com/nmstreethran/ml-elec-model.git
```

**Using SSH:**

```sh
git clone --recurse-submodules git@github.com:nmstreethran/ml-elec-model.git
```

## Documentation

Documentation is written in the repository's [GitHub Wiki](https://github.com/nmstreethran/ml-elec-model/wiki). The files can also be found in the [`docs`](docs/) folder.

The GitHub wiki has been included in this repository as a submodule. Once changes to the wiki within the submodule are made (e.g., new markdown files, images), these changes are first committed and pushed to the wiki's branch, before committing and pushing to the main repository's branch.

To compile the documentation after cloning the repository, run the following bash script:

```sh
bash docs.sh
```

## License

Unless otherwise stated:

- Python scripts, Jupyter notebooks and any other form of code or snippets (e.g., shell scripts) in this repository are licensed under the [MIT License](https://opensource.org/licenses/MIT).
- content, images and documentation are licensed under the [Creative Commons Attribution 4.0 International (CC BY 4.0) License](https://creativecommons.org/licenses/by/4.0/).

## Credits

The documentation is compiled using Pandoc.
Pandoc is Copyright (c) 2006-2019 John MacFarlane (jgm at berkeley dot edu), released under the [GNU General Public License version 2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) or later.

[`pandoc.latex`](docs/pandoc.latex), a LaTeX template for formatting PDFs generated using Pandoc and a LaTeX PDF engine, originally downloaded from the [Pandoc repository](https://github.com/jgm/pandoc/blob/master/data/templates/default.latex), and modified by Nithiya Streethran.

[`syntax.theme`](docs/syntax.theme), a Syntax highlighting theme for Pandoc, originally downloaded from the [skylighting repository](https://github.com/jgm/skylighting/blob/master/skylighting-core/test/default.theme), and modified by Nithiya Streethran.
skylighting is is Copyright (c) John MacFarlane (jgm at berkeley dot edu), released under the [GNU General Public License version 2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) or later, and skylighting-core is released under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

The documentation in PDF format incorporates the following fonts:

- [EB Garamond by Georg Duffner](https://fonts.google.com/specimen/EB+Garamond), licensed under the [SIL Open Font License](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL_web).
- [Lato by Łukasz Dziedzic](https://fonts.google.com/specimen/Lato), licensed under the [SIL Open Font License](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL_web).
- [Fira Code by Nikita Prokopov](https://github.com/tonsky/FiraCode), licensed under the [SIL Open Font License](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL_web).

Badges are generated using [Shields.io](https://shields.io).
Shields.io is licensed under a [Creative Commons Zero v1.0 Universal License](https://creativecommons.org/publicdomain/zero/1.0/).

Icons used within badges are from [Simple Icons](https://simpleicons.org/).
Simple Icons is licensed under a [Creative Commons Zero v1.0 Universal License](https://creativecommons.org/publicdomain/zero/1.0/).

The Creative Commons license in markdown format is imported from [idleberg/Creative-Commons-Markdown](https://github.com/idleberg/Creative-Commons-Markdown).

This repository is a continuation and improvement of the work done by Nithiya Streethran in [ENSYSTRA/short-term-forecasting](https://github.com/ENSYSTRA/short-term-forecasting).
ENSYSTRA is funded by the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No: 765515.

Contributing guidelines are adapted from the [Open Science MOOC](https://github.com/OpenScienceMOOC/Module-5-Open-Research-Software-and-Open-Source). The contents of the MOOC are licensed under a [Creative Commons Zero v1.0 Universal License](https://creativecommons.org/publicdomain/zero/1.0/).
