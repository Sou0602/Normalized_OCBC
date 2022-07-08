#!/usr/bin/env python

import doodad as dd
import gcsl.doodad_utils as dd_utils
import argparse
import pdb
def run(output_dir='/tmp', env_name='pusher', gpu=True, seed=0,K =0, **kwargs):

    import gym
    import numpy as np
    from rlutil.logging import log_utils, logger

    import rlutil.torch as torch
    import rlutil.torch.pytorch_util as ptu

    # Envs

    from gcsl import envs
    from gcsl.envs.env_utils import DiscretizedActionEnv

    # Algo
    from gcsl.algo import buffer,variants_n11, networks_n11, gcsl_n11_sto

    ptu.set_gpu(gpu)
    if not gpu:
        print('Not using GPU. Will be slow.')

    torch.manual_seed(seed)
    np.random.seed(seed)

    env = envs.create_env(env_name)
    env_params = envs.get_env_params(env_name)
    print(env_params)

    env, policy, replay_buffer, gcsl_kwargs = variants_n11.get_params(env, env_params)

    if K == 2:
        algo = gcsl_n11_sto.GCSL(
        env,
        policy,
        replay_buffer,
        **gcsl_kwargs
        )


    exp_prefix = 'example/%s/norm_biased_s%d_%d/' % (env_name,K,seed)

    with log_utils.setup_logger(exp_prefix=exp_prefix, log_base_dir=output_dir):
        algo.train()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-S","--seed",default = '0' )
    parser.add_argument("-E","--env",default='pointmass_rooms')
    parser.add_argument("-K","--rep",default='0')

    args = parser.parse_args()
    seed = int(args.seed)
    env = args.env
    k = int(args.rep)
    #pdb.set_trace()
    params = {
        'seed': [seed],
        'env_name': [env], #['lunar', 'pointmass_empty','pointmass_rooms', 'pusher', 'claw', 'door'],
        'K':[k],
        'gpu': [True],
    }
    dd_utils.launch(run, params, mode='local', instance_type='c4.xlarge')
