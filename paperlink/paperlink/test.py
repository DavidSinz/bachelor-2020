import inotify.adapters

i = inotify.adapters.Inotify()

i.add_watch('app.py')


for event in i.event_gen(yield_nones=False):
    (_, type_names, path, filename) = event

    print("PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(path, filename, type_names))
