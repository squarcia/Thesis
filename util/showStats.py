import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#   Bool field
#   1 = Days
#   0 = Weeks

def show(df_followers, bool):

    # +++++ È utile per vedere quali profili hanno più followers (serve per verifica dev. std) +++++
    #print(df_followers_7gg.nlargest(10, '1Day'))

    # Calculate, for each column, standard deviation
    stds_array = df_followers.std()

    # Calculate, for each column, average
    df_avg = df_followers.mean()
    df_avg_new = np.array(df_avg.values)

    # Delete the inf value at the top of array
    avg_array = np.delete(df_avg_new, 0)

    if (bool): 

        days = range(1, 8)

        # Plot mean
        plt.plot(days, avg_array, label = "Avg")

        # Plot std dev
        plt.plot(days, stds_array, label = "Dev. Std.")

        plt.xlabel('Days')

    else:

        weeks = range(1, 5)

        # Plot mean
        plt.plot(weeks, avg_array, label = "Avg")

        # Plot std dev
        plt.plot(weeks, stds_array, label = "Dev. Std.")

        plt.xlabel('Weeks')  

    # Set y-label
    plt.ylabel('Followers')

    # Set title
    plt.title('Average and dev. std. followers')

    # Set legend
    plt.legend()

    # Show plot
    plt.show()