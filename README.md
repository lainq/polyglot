<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Polyglot</h3>

  <p align="center">
    Find the percentage of programming languages used in your project
    <br />
    <a href="https://github.com/pranavbaburaj/polyglot/tree/main/docs">Documentation</a>
    ·
    <a href="https://github.com/pranavbaburaj/polyglot/issues">Report a Bug</a>
    ·
    <a href="https://github.com/pranavbaburaj/polyglot/pulls">Request Feature</a>
  </p>
  <br />

</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Initial Setup](#initial-setup)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

<!-- ABOUT THE PROJECT -->

## About The Project

Find the percentage of programming languages used in your project

<!-- GETTING STARTED -->

## Getting Started

In order to get started, please install pip.

### Prerequisites

- pip

```sh
sudo apt-get install python3-pip
```

### Installation

- Install pip packages

```sh
pip3 install python-polyglot
```

## Usage

Once Polyglot is all setup and good to go, implementing is easy as pie.

### Initial Setup

You can initialize Polyglot with the example below:

```python
from polyglot.core import Polyglot

dirname = "path/to/directory"

polyglot = Polyglot(dirname)
polyglot.show(display=True)

```

```
+-------------------------+-------+
|         Language        | files |
+-------------------------+-------+
|       Ignore List       |  5.88 |
| GCC Machine Description | 11.76 |
|          Unknown        |  5.88 |
|           Text          |  5.88 |
|          Python         | 64.71 |
|           JSON          |  5.88 |
+-------------------------+-------+


+-------------------------+-------+
|         Language        | lines |
+-------------------------+-------+
|       Ignore List       | 17.22 |
| GCC Machine Description | 22.24 |
|         Unknown         |  2.83 |
|           Text          |  0.26 |
|          Python         | 57.07 |
|           JSON          |  0.39 |
+-------------------------+-------+
```

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature`)
3. Commit your Changes (`git commit -m 'Add some features'`)
4. Push to the Branch (`git push origin feature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT license. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Pranav Baburaj - pranavbaburaj@zohomail.com
