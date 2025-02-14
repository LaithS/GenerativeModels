"""AE.py:  Autoencoder methods"""
__author__      = "Khalid M. Kahloot"
__copyright__   = "Copyright 2019, Only for profesionals"


import os
import tensorflow as tf
import numpy as np
import sys
sys.path.append('..')

from .AE_BASE import AE_BASE
import _utils.utils as utils
import _utils.constants as const

class AE(AE_BASE):
    def __init__(self, *argz, **kwrds):
        super(AE, self).__init__(*argz, **kwrds)
        self.config.model_name = 'AE'
        self.config.model_type = const.AE
        self.setup_logging()
        
    def _build(self):
       
        '''  ---------------------------------------------------------------------
                            COMPUTATION GRAPH (Build the model)
        ---------------------------------------------------------------------- '''
        from Alg_AE.AE_model import AEModel
        self.model = AEModel(self.network_params,sigma_act=utils.softplus_bias,
                               transfer_fct=tf.nn.relu, learning_rate=self.config.l_rate,
                               kinit=tf.contrib.layers.xavier_initializer(),
                               batch_size=self.config.batch_size, dropout=self.config.dropout, batch_norm=self.config.batch_norm, 
                               epochs=self.config.epochs, checkpoint_dir=self.config.checkpoint_dir, 
                               summary_dir=self.config.summary_dir, result_dir=self.config.results_dir, 
                               restore=self.flags.restore, plot=self.flags.plot, model_type=self.config.model_type)
        print('building AE Model...')
        print('\nNumber of trainable paramters', self.model.trainable_count)
        
    
    def animate(self):
        return self.model.animate()

    '''  
    ------------------------------------------------------------------------------
                                         MODEL OPERATIONS
    ------------------------------------------------------------------------------ 
    '''    
              
    def encode(self, inputs):
        '''  ------------------------------------------------------------------------------
                                         DATA PROCESSING
        ------------------------------------------------------------------------------ '''           
        inputs = utils.prepare_dataset(inputs) 
        return self.model.encode(inputs)
        
    def decode(self, z):
        return self.model.decode(z)
     
    def interpolate(self, input1, input2):
        input1 = utils.prepare_dataset(input1)
        input2 = utils.prepare_dataset(input2)         
        return self.model.interpolate(input1, input2)

    def reconst_loss(self, inputs):
        '''  ------------------------------------------------------------------------------
                                         DATA PROCESSING
        ------------------------------------------------------------------------------ '''           
        inputs = utils.prepare_dataset(inputs) 
        return self.model.reconst_loss(inputs)