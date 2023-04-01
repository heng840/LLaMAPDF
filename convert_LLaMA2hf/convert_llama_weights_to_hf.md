# some tips
* You are viewing main version, which requires installation from source. 
If you use pip install transformers, you will not be able to use LLaMA
```bash
pip install git+https://github.com/huggingface/transformers

git clone https://github.com/huggingface/transformers.git
```
* Then the model weight of LLaMA is converted into the form of hugging face model. There is no need to change the parameters, 
directly use 
```bash 
bash bash_convert.sh
```
this operation will be performed in the source code of transformers.
* After conversion, the model and tokenizer can be loaded via:
```python
from transformers import LlamaForCausalLM, LlamaTokenizer
tokenizer = LlamaTokenizer.from_pretrained("/output/path")
model = LlamaForCausalLM.from_pretrained("/output/path")
```
