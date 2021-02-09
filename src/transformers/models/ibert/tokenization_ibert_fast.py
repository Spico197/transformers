# coding=utf-8
# Copyright 2018 The Open AI Team Authors and The HuggingFace Inc. team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ...utils import logging
from ..roberta.tokenization_roberta_fast import RobertaTokenizerFast
from .tokenization_ibert import IBertTokenizer


logger = logging.get_logger(__name__)

PRETRAINED_VOCAB_FILES_MAP = {
    "vocab_file": {
        "ibert-roberta-base": "https://huggingface.co/roberta-base/resolve/main/vocab.json",
        "ibert-roberta-large": "https://huggingface.co/roberta-large/resolve/main/vocab.json",
        "ibert-roberta-large-mnli": "https://huggingface.co/roberta-large-mnli/resolve/main/vocab.json",
    },
    "merges_file": {
        "ibert-roberta-base": "https://huggingface.co/roberta-base/resolve/main/merges.txt",
        "ibert-roberta-large": "https://huggingface.co/roberta-large/resolve/main/merges.txt",
        "ibert-roberta-large-mnli": "https://huggingface.co/roberta-large-mnli/resolve/main/merges.txt",
    },
    "tokenizer_file": {
        "ibert-roberta-base": "https://huggingface.co/roberta-base/resolve/main/tokenizer.json",
        "ibert-roberta-large": "https://huggingface.co/roberta-large/resolve/main/tokenizer.json",
        "ibert-roberta-large-mnli": "https://huggingface.co/roberta-large-mnli/resolve/main/tokenizer.json",
    },
}

PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES = {
    "ibert-roberta-base": 512,
    "ibert-roberta-large": 512,
    "ibert-roberta-large-mnli": 512,
}

class IBertTokenizerFast(RobertaTokenizerFast):
    r"""
    Construct a "fast" I-BERT tokenizer (backed by HuggingFace's `tokenizers` library).

    :class:`~transformers.IBertTokenizerFast` is identical to :class:`~transformers.RobertaTokenizerFast`. Refer to
    superclass :class:`~transformers.RobertaTokenizerFast` for usage examples and documentation concerning the
    initialization parameters and other methods.
    """
    # merges and vocab same as Roberta
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    slow_tokenizer_class = IBertTokenizer
