import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def showDaysStats(df_followers_7gg):

    # +++++ È utile per vedere quali profili hanno più followers (serve per verifica dev. std) +++++
    #print(df_followers_7gg.nlargest(10, '1Day'))

    # Calculate, for each column, standard deviation
    stds_array = df_followers_7gg.std()

    # Calculate, for each column, average
    df_avg_days = df_followers_7gg.mean()
    df_avg_days_new = np.array(df_avg_days.values)

    # Delete the inf value at the top of array
    avg_array = np.delete(df_avg_days_new, 0)

    days = range(1, 8)

    # Plot mean
    plt.plot(days, avg_array, label = "Avg")

    # Plot std dev
    plt.plot(days, stds_array, label = "Dev. Std.")

    # Set x-label
    plt.xlabel('Days')

    # Set y-label
    plt.ylabel('Followers')

    # Set title
    plt.title('Average and dev. std. followers')

    # Set legend
    plt.legend()

    # Show plot
    plt.show()



def showWeeksStats(df_followers_4week):

    # +++++ È utile per vedere quali profili hanno più followers (serve per verifica dev. std) +++++
    #print(df_followers_4week.nlargest(10, '4Week'))

    # Calculate, for each column, standard deviation
    stds_array = df_followers_4week.std()

    # Calculate, for each column, average
    df_avg_weeks = df_followers_4week.mean()
    df_avg_weeks_new = np.array(df_avg_weeks.values)

    # Delete the inf value at the top of array
    avg_array = np.delete(df_avg_weeks_new, 0)

    weeks = range(1, 5)

    # Plot mean
    plt.plot(weeks, avg_array, label = "Avg")

    # Plot std dev
    plt.plot(weeks, stds_array, label = "Dev. Std.")

    # Set x-label
    plt.xlabel('Weeks')

    # Set y-label
    plt.ylabel('Followers')

    # Set title
    plt.title('Average and dev. std. followers')

    # Set legend
    plt.legend()

    # Show plot
    plt.show()










