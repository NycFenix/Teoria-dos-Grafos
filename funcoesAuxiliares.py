import gc

def destroy(objeto):
    del(objeto)
    gc.collect()