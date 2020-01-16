# -*- coding: utf-8 -*-
#@author emirhanylmzz

import tensorflow as tf
import numpy as np

head_size = np.array([4512, 3738, 4261, 3777, 4177, 3585, 3785, 3559, 3613, 3982, 3443, 3993, 3640, 4208, 3832, 3876, 3497, 3466, 3095, 4424, 3878, 4046, 3804, 3710, 4747, 4423, 4036, 4022, 3454, 4175, 3787, 3796, 4103, 4161, 4158, 3814, 3527, 3748, 3334, 3492, 3962, 3505, 4315, 3804, 3863, 4034, 4308, 3165, 3641, 3644, 3891, 3793, 4270, 4063, 4012, 3458, 3890], dtype = float)
brain_weight = np.array([1530, 1297, 1335, 1282, 1590, 1300, 1400, 1255, 1355, 1375, 1340, 1380, 1355, 1522, 1208, 1405, 1358, 1292, 1340, 1400, 1357, 1287, 1275, 1270, 1635, 1505, 1490, 1485, 1310, 1420, 1318, 1432, 1364, 1405, 1432, 1207, 1375, 1350, 1236, 1250, 1350, 1320, 1525, 1570, 1340, 1422, 1506, 1215, 1311, 1300, 1224, 1350, 1335, 1390, 1400, 1225, 1310], dtype = float)

l0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([l0])

model.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss='mean_squared_error')

history = model.fit(head_size, brain_weight, epochs=500, verbose=False)

print(model.predict([3832]))

print("These are the layer variables: {}".format(l0.get_weights()))
