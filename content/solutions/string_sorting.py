from IPython.html.widgets import TextWidget
@interact
def sort_string(s:TextWidget() , reverse=False):
    s = reversed(sorted(s)) if reverse else sorted(s)
    print (''.join(s))
