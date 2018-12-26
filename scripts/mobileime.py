# Mobile-like Display
from ipywidgets import widgets
from IPython.display import display
from spellingcorrector import candidates, correction
from dictionarycontingency import hanzi

output = widgets.Textarea(description = "Output: ")
pinyin = widgets.Text(description = "Pinyin Input: ")
select = widgets.ToggleButtons(options=hanzi[correction("")][0:5], description = "Select: ")

def pinyin_handler(sender):
    select.index = None
    select.options = hanzi[correction(pinyin.value)][0:5]
    output.value = output.value + select.value
    # select.observe(on_click, "value")
    pinyin.value = ""

        

        
def on_click(change):
    output.value = output.value[:-1] + select.value
    pinyin.index = ""



display(output)
pinyin.on_submit(pinyin_handler)
display(select)
display(pinyin)