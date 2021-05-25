import numpy as np
import matplotlib.pyplot as plt
import util.calculate as cf

#   TIPS: 
#   
#   PERIOD: 
#       - first_week: show first 7 days
#       - first_month: show first 4 weeks
#
#   TYPE: 
#       - Word used on y axis on graphs


def showBoxPlots(df, period, type):

    array_columns = []

    for column in df.columns[1:]:

        # Convert Series to array
        temp = df[column].to_numpy()

        # Filter and remove all the NaN values (due to boxplot error)
        filtered_data = temp[~np.isnan(temp)]

        # Add element to list
        array_columns.append(filtered_data)
    

    # Set plot settings
    fig, ax = plt.subplots()

    if (period == "first_week"):

        ax.set_title('First Week')
        ax.set_xlabel('Days')
        
    elif (period == "first_month"):

        ax.set_title('First Four Weeks')
        ax.set_xlabel('Weeks')

    # Get type value and display it on y axis
    ax.set_ylabel(type)
    
    # Plot 
    ax.boxplot(array_columns, showfliers=True)



    #   ---------- *** ----------
    #   CALCULATE AGGREGATE VALUES
    #   ---------- *** ----------


    # Calculate avg for each days/weeks
    df_avg = df.mean()
    df_avg_new = np.array(df_avg.values)
    avg_array = np.delete(df_avg_new, 0)

    # Calculate std. dev for each days/weeks
    stds_array = df.std().to_numpy()
    
    # Calculate max for each days/weeks
    _max = np.array(df.max())
    _max_weeks = np.delete(_max, 0)

    row_labels=['Avg','Std. Dev.','Max']

    if (period == "first_week"):
        col_labels=["1Day", "2Day", "3Day", "4Day", "5Day", "6Day", "7Day"]
    elif (period == "first_month"):
        col_labels=['1Week','2Week','3Week', "4Week"]

    # Generate plot 
    fig1, ax1 = plt.subplots(1,1)

    # Create table values
    table_vals = [avg_array, stds_array, _max_weeks]

    # Create table
    ax1.table(cellText=table_vals, colLabels=col_labels, rowLabels=row_labels, loc="center")

    plt.axis('off')

    # Show plots
    plt.show()


def showBins(groupby_df, type):

    bins_1st_day, bins_7_days, bins_28_days =  cf.getBins(groupby_df, type)

    
    plt.hist(bins_1st_day, bins=range(0, max(bins_1st_day) + 10, 10), log=True)
    #plt.xticks(range(0, max(arr) + 10, 10))
    if (type == "statuses_count"):
        plt.title("Tweets 1st Day")
    elif (type == "followers_count"):
        plt.title("Followers 1st Day")
    else:
        plt.title("Friends 1st Day")

    plt.ylabel("Counts")
    plt.xlabel("Bins")
    plt.grid(True) 
    plt.show()

    plt.hist(bins_7_days, bins=range(0, max(bins_7_days) + 10, 10), log=True)
    #plt.xticks(range(0, max(arr) + 10, 10))
    if (type == "statuses_count"):
        plt.title("Tweets 7 Days")
    elif (type == "followers_count"):
        plt.title("Followers 7 Days")
    else:
        plt.title("Friends 7 Days")
        
    plt.ylabel("Counts")
    plt.xlabel("Bins")
    plt.grid(True) 
    plt.show()

    plt.hist(bins_28_days, bins=range(0, max(bins_28_days) + 10, 10), log=True)
    #plt.xticks(range(0, max(arr) + 10, 10))
    if (type == "statuses_count"):
        plt.title("Tweets 28 Days")
    elif (type == "followers_count"):
        plt.title("Followers 28 Days")
    else:
        plt.title("Friends 28 Days")
        
    plt.ylabel("Counts")
    plt.xlabel("Bins")
    plt.grid(True) 
    plt.show()
    
