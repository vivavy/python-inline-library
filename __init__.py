# -*- coding: utf-8 -*-
# @Author  : vi_is_lonely
# @Time    : 2024/09/03
# @File    : inline.py
# @Project : python-inline-library
# @Desc    : Inline library specially for _k_bar_n_
# @Github  : https://github.com/vivavy/python-inline-library
# @License: GPL-3.0

# Copyright (c) 2024 Ivan CHetchasov

def inline(path: str) -> None:
    """
    Inline file as C-style include
    :param path: path to file to inline
    :return: NoneType
    """
    with open(path, "rt") as f:
        return compile(f.read())
