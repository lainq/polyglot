<!-- PROJECT LOGO -->

<br />
<p align="center">
  <img src="https://user-images.githubusercontent.com/70764593/114295267-c9cdb780-9ac1-11eb-94aa-f864328d6845.png" aly="logo">
  <h3 align="center">Polyglot</h3>

  <p align="center">
    Find the percentage of programming languages used in your project
    <br />
    <a href="https://github.com/pranavbaburaj/polyglot/blob/main/docs/README.md">📖 Documentation</a>
    ·
    <a href="https://github.com/pranavbaburaj/polyglot/issues">Report a Bug</a>
    ·
    <a href="https://github.com/pranavbaburaj/polyglot/pulls">Request Feature</a>
  </p>
  <br>
  <p align="center">
    <img src="https://static.pepy.tech/badge/python-polyglot">
    <img src="https://img.shields.io/discord/808537055177080892.svg">
    <img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103">
    <img src="https://img.shields.io/github/last-commit/pranavbaburaj/polyglot">
    <a href="https://twitter.com/intent/tweet?text=Find%20the%20percentage%20of%20programming%20languages%20in%20your%20project&url=https://github.com/pranavbaburaj/polyglot&via=baburaj_pranav&hashtags=developers,polyglot,language"><img src="https://img.shields.io/twitter/url/http/shields.io.svg?style=social"></a>
    <img src="https://tokei.rs/b1/github/pranavbaburaj/polyglot">
    <img src="https://api.codacy.com/project/badge/Grade/601da323f4ea482f9c2ee7f4164e8ee9">
  </p>


  <br />

</p>


## About The Project

Find the percentage of programming languages used in your project

<!-- GETTING STARTED -->

## ⚡ Getting Started

In order to get started, please make sure that you have [`python`](https://python.org) and `pip` installed on your computer.


### ⬇️ Installation

- Install pip packages

```sh
# install the python-polyglot package using pip

pip3 install python-polyglot
# or
pip install python-polyglot
```

## 🎉 Usage

Once Polyglot is all setup and good to go, implementing is easy as pie.

### 🔰 Initial Setup

You can initialize Polyglot with the example below:

```python
from polyglot.core import Polyglot

dirname = "path/to/directory"

polyglot = Polyglot(dirname)
polyglot.show(display=True)
```

Read the complete polyglot documentation [here](https://github.com/pranavbaburaj/polyglot/blob/main/docs/README.md)

<br>
<img src="https://github.com/pranavbaburaj/polyglot/blob/main/docs/polyglot-result.png?raw=true" height="450">

> Read more about the documentation [here](https://github.com/pranavbaburaj/polyglot/blob/main/docs/README.md)

<!--
```
+-------------------------+---------+-------+-------+
|         Language        |  Files  | Total | Blank |
+-------------------------+---------+-------+-------+
|       Unknown file      | 13.89 % |   5   |   0   |
|           YAML          |  2.78 % |   1   |   0   |
| GCC Machine Description |  8.33 % |   3   |   0   |
|           Text          | 13.89 % |   5   |   0   |
|          Python         | 55.56 % |   20  |   0   |
|           TOML          |  2.78 % |   1   |   0   |
|           JSON          |  2.78 % |   1   |   0   |
+-------------------------+---------+-------+-------+


+-------------------------+---------+-------+-------+
|         Language        |  Lines  | Total | Blank |
+-------------------------+---------+-------+-------+
|       Unknown file      | 29.67 % |  3491 |  101  |
|           YAML          | 58.35 % |  6865 |   1   |
| GCC Machine Description |  2.97 % |  349  |   90  |
|           Text          |  0.31 % |   36  |   4   |
|          Python         |  8.07 % |  949  |  205  |
|           TOML          |  0.59 % |   70  |   14  |
|           JSON          |  0.04 % |   5   |   0   |
+-------------------------+---------+-------+-------+
```
-->

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. [Fork](https://github.com/pranavbaburaj/polyglot/fork) the Project
2. Create your Feature Branch (`git checkout -b feature`)
3. Commit your Changes (`git commit -m 'Add some features'`)
4. Push to the Branch (`git push origin feature`)
5. Open a Pull Request


