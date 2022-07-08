import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
env = 'pointmass_rooms'

##unbiased_norm
n_df_gcsl_0 = pd.read_csv('unbiased_norm/seed_0/progress.csv')
n_df_gcsl_1 = pd.read_csv('unbiased_norm/seed_1/progress.csv')
n_df_gcsl_2 = pd.read_csv('unbiased_norm/seed_2/progress.csv')
n_df_gcsl_3 = pd.read_csv('unbiased_norm/seed_3/progress.csv')
n_df_gcsl_4 = pd.read_csv('unbiased_norm/seed_4/progress.csv')

##biased_norm
# n_df_gcsl_0 = pd.read_csv('biased_norm/seed_0/progress.csv')
# n_df_gcsl_1 = pd.read_csv('biased_norm/seed_1/progress.csv')
# n_df_gcsl_2 = pd.read_csv('biased_norm/seed_2/progress.csv')
# n_df_gcsl_3 = pd.read_csv('biased_norm/seed_3/progress.csv')
# n_df_gcsl_4 = pd.read_csv('biased_norm/seed_4/progress.csv')

#'''''
##unbiased_eps_0.1
# n_df_gcsl_0 = pd.read_csv('unbiased_eps_0.1/seed_0/progress.csv')
# n_df_gcsl_1 = pd.read_csv('unbiased_eps_0.1/seed_1/progress.csv')
# n_df_gcsl_2 = pd.read_csv('unbiased_eps_0.1/seed_2/progress.csv')
# n_df_gcsl_3 = pd.read_csv('unbiased_eps_0.1/seed_3/progress.csv')
# n_df_gcsl_4 = pd.read_csv('unbiased_eps_0.1/seed_4/progress.csv')

#biased_eps_0.1
# n_df_gcsl_0 = pd.read_csv('biased_eps_0.1/seed_0/progress.csv')
# n_df_gcsl_1 = pd.read_csv('biased_eps_0.1/seed_1/progress.csv')
# n_df_gcsl_2 = pd.read_csv('biased_eps_0.1/seed_2/progress.csv')
# n_df_gcsl_3 = pd.read_csv('biased_eps_0.1/seed_3/progress.csv')
# n_df_gcsl_4 = pd.read_csv('biased_eps_0.1/seed_4/progress.csv')
##unbiased_eps_0.01
# n_df_gcsl_0 = pd.read_csv('unbiased_eps_0.01/seed_0/progress.csv')
# n_df_gcsl_1 = pd.read_csv('unbiased_eps_0.01/seed_1/progress.csv')
# n_df_gcsl_2 = pd.read_csv('unbiased_eps_0.01/seed_2/progress.csv')
# n_df_gcsl_3 = pd.read_csv('unbiased_eps_0.01/seed_3/progress.csv')
# n_df_gcsl_4 = pd.read_csv('unbiased_eps_0.01/seed_4/progress.csv')

# #biased eps_0.01
# n_df_gcsl_0 = pd.read_csv('biased_eps_0.01/seed_0/progress.csv')
# n_df_gcsl_1 = pd.read_csv('biased_eps_0.01/seed_1/progress.csv')
# n_df_gcsl_2 = pd.read_csv('biased_eps_0.01/seed_2/progress.csv')
# n_df_gcsl_3 = pd.read_csv('biased_eps_0.01/seed_3/progress.csv')
# n_df_gcsl_4 = pd.read_csv('biased_eps_0.01/seed_4/progress.csv')

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


n_stack_success = np.hstack((n_success_0,n_success_1,n_success_2,n_success_3,n_success_4))
n_stack_success = np.reshape(n_stack_success,(-1,5))
n_success = np.mean(n_stack_success,axis = 1)
std_n_success = np.std(n_stack_success,axis = 1)
#
#plt.plot(time_0,success_0,'b', label = 'Normalized OCBC')
#plt.plot(n_time_0,n_success,'r', label = 'Normalized OCBC - drop w')
#plt.fill_between(n_time_0,n_success - std_n_success , n_success + std_n_success,color = 'r' , alpha = 0.2)

# plt.plot(n_time_0,n_success_0,'r', label = 'Norm - drop w - 0')
# plt.plot(n_time_1,n_success_1,'g', label = 'Norm - drop w - 1')
# plt.plot(n_time_2,n_success_2,'k', label = 'Norm - drop w - 2')
# plt.plot(n_time_3,n_success_3,'m', label = 'Norm - drop w - 3')
# plt.plot(n_time_4,n_success_4,'c', label = 'Norm - drop w - 4')


plt.xlabel('TimeSteps')
plt.ylabel('Success')
plt.legend()
plt.title('Success-' + env +'(eps = 0.1)')
plt.grid()
plt.show()

plt.close()






