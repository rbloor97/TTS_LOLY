import tensorflow as tf

with tf.Session(config=tf.ConfigProto(allow_soft_placement=True, \
                log_device_placement=True)) as sess:
    saver = tf.train.import_meta_graph('checkpoints01/tacotron_model.ckpt-47500.meta')
    saver.restore(sess, "checkpoints01/tacotron_model.ckpt-47500")

Cambios realizados,
En la carpeta tacotron reemplazar los archivos
en el hparams.py cambia a english_cleaners
en synthesize.py reemplazar los archivos