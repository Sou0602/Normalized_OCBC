import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
env = 'pointmass_rooms'

#pusher
#'''''
##unbiased_eps_0.1
# df_gcsl_0 = pd.read_csv('data/example/pointmass_rooms/norm_s0_0/2022_06_01_10_52_11/progress.csv')
# n_df_gcsl_0 = pd.read_csv('data/example/pointmass_rooms/norm_s0_0/2022_06_01_21_53_58/progress.csv')
# n_df_gcsl_1 = pd.read_csv('data/example/pointmass_rooms/norm_unbiased_s0_1/2022_06_05_18_18_47/progress.csv')
# n_df_gcsl_2 = pd.read_csv('data/example/pointmass_rooms/norm_unbiased_s0_2/2022_06_05_16_44_10/progress.csv')
# n_df_gcsl_3 = pd.read_csv('data/example/pointmass_rooms/norm_unbiased_s0_3/2022_06_05_18_18_47/progress.csv')
# n_df_gcsl_4 = pd.read_csv('data/example/pointmass_rooms/norm_unbiased_s0_4/2022_06_05_18_18_47/progress.csv')

#biased_eps_0.1
# df_gcsl_0 = pd.read_csv('data/example/pointmass_rooms/norm_s0_0/2022_06_01_11_21_20/progress.csv')
# n_df_gcsl_0 = pd.read_csv('data/example/pointmass_rooms/norm_biased_s0_6/2022_06_06_00_05_08/progress.csv')
# n_df_gcsl_1 = pd.read_csv('data/example/pointmass_rooms/norm_biased_s0_1/2022_06_05_23_04_15/progress.csv')
# n_df_gcsl_2 = pd.read_csv('data/example/pointmass_rooms/norm_biased_s0_7/2022_06_06_00_05_08/progress.csv')
# n_df_gcsl_3 = pd.read_csv('data/example/pointmass_rooms/norm_biased_s0_3/2022_06_05_23_04_15/progress.csv')
# n_df_gcsl_4 = pd.read_csv('data/example/pointmass_rooms/norm_biased_s0_4/2022_06_05_23_04_15/progress.csv')
##unbiased_eps_0.01
# df_gcsl_0 = pd.read_csv('data/example/pointmass_rooms/norm_s0_0/2022_06_01_10_52_11/progress.csv')
# n_df_gcsl_0 = pd.read_csv('data/example/pointmass_rooms/norm_unbiased_s1_1/2022_06_06_08_25_10/progress.csv')
# n_df_gcsl_1 = pd.read_csv('data/example/pointmass_rooms/norm_unbiased_s1_2/2022_06_06_08_25_10/progress.csv')
# n_df_gcsl_2 = pd.read_csv('data/example/pointmass_rooms/norm_unbiased_s1_3/2022_06_06_08_25_10/progress.csv')
# n_df_gcsl_3 = pd.read_csv('data/example/pointmass_rooms/norm_unbiased_s1_4/2022_06_06_08_25_10/progress.csv')
# n_df_gcsl_4 = pd.read_csv('data/example/pointmass_rooms/norm_unbiased_s1_8/2022_06_06_09_26_59/progress.csv')

# #biased eps_0.01
df_gcsl_0 = pd.read_csv('data/example/pointmass_rooms/norm_s0_0/2022_06_01_11_21_20/progress.csv')
n_df_gcsl_0 = pd.read_csv('data/example/pointmass_rooms/norm_biased_s1_1/2022_06_06_02_51_43/progress.csv')
n_df_gcsl_1 = pd.read_csv('data/example/pointmass_rooms/norm_biased_s1_2/2022_06_06_02_51_44/progress.csv')
n_df_gcsl_2 = pd.read_csv('data/example/pointmass_rooms/norm_biased_s1_6/2022_06_06_03_52_36/progress.csv')
n_df_gcsl_3 = pd.read_csv('data/example/pointmass_rooms/norm_biased_s1_8/2022_06_06_03_52_37/progress.csv')
n_df_gcsl_4 = pd.read_csv('data/example/pointmass_rooms/norm_biased_s1_5/2022_06_06_03_52_37/progress.csv')
#r_df_gcsl_0 = pd.read_csv('data/example/door/gcsl_r_online0_0/2022_03_29_17_27_04/progress.csv')

time_0 = df_gcsl_0['Validation loss'].values
success_0 = df_gcsl_0['Eval success ratio'].values

n_time_0 = n_df_gcsl_0['Validation loss'].values
n_success_0 = n_df_gcsl_0['Eval success ratio'].values

n_time_1 = n_df_gcsl_1['Validation loss'].values
n_success_1 = n_df_gcsl_1['Eval success ratio'].values

n_time_2 = n_df_gcsl_2['Validation loss'].values
n_success_2 = n_df_gcsl_2['Eval success ratio'].values

n_time_3 = n_df_gcsl_3['Validation loss'].values
n_success_3 = n_df_gcsl_3['Eval success ratio'].values

n_time_4 = n_df_gcsl_4['Validation loss'].values
n_success_4 = n_df_gcsl_4['Eval success ratio'].values
# r_time_0 = r_df_gcsl_0['timesteps'].values
# r_success_0 = r_df_gcsl_0['Eval success ratio'].values

n_stack_success = np.hstack((n_success_0,n_success_1,n_success_2,n_success_3,n_success_4))
n_stack_success = np.reshape(n_stack_success,(-1,5))
n_success = np.mean(n_stack_success,axis = 1)
std_n_success = np.std(n_stack_success,axis = 1)
#
#plt.plot(time_0,success_0,'b', label = 'Normalized OCBC')
#plt.plot(n_time_0,n_success,'r', label = 'Normalized OCBC - drop w')
#plt.fill_between(n_time_0,n_success - std_n_success , n_success + std_n_success,color = 'r' , alpha = 0.2)
plt.plot(n_time_0,n_success_0,'r', label = 'Norm - drop w - 0')
plt.plot(n_time_1,n_success_1,'g', label = 'Norm - drop w - 1')
plt.plot(n_time_2,n_success_2,'k', label = 'Norm - drop w - 2')
plt.plot(n_time_3,n_success_3,'m', label = 'Norm - drop w - 3')
plt.plot(n_time_4,n_success_4,'c', label = 'Norm - drop w - 4')
#plt.plot(r_time_0,r_success_0,'g',label = 'Ratio')


plt.xlabel('TimeSteps')
plt.ylabel('Success')
plt.legend()
plt.title('Success-' + env +'(eps = 0.1)')
plt.grid()
plt.show()
#plt.savefig('plots_new/'+env+'_loss/Success.jpg')
plt.close()






