import pandas as pd
import matplotlib.pyplot as plot
import os.path


def main():
    # Setting input parameters and the input and output file names
    input_file_name = 'btc.csv'
    summary_file_name = 'summary.csv'
    usd_to_eur_rate = 0.87

    # check if the file exists
    if not(os.path.isfile(input_file_name)):
        print('input file does not exist')
        exit()

    # Reading the bicoin price csv file
    data = pd.read_csv(input_file_name, parse_dates=['Date'], encoding="utf-8")

    # Sort the records based on the date as we take the latest 365 days for summary
    data.sort_values(by=['Date'], inplace=True)

    # Separating the last 365 days of the records
    new_data = data[['Date', 'Volume', 'Low', 'High']].tail(365)

    # converting the usd to eur rate and volume to billions
    new_data[['Low', 'High']] = new_data[['Low', 'High']] * usd_to_eur_rate
    new_data[['Volume']] = new_data[['Volume']] / 10**9

    # Changing the column names to new ones as per the summary file format requested
    new_data.rename(columns={'Low': 'Low (EUR)',
                             'High': 'High (EUR)', 'Volume': 'Volume (Billion)'}, inplace=True)

    # Setting the decimal format and printing the requested info
    pd.options.display.float_format = '{:.2f}'.format
    print(new_data[['Low (EUR)', 'High (EUR)', 'Volume (Billion)']].agg(
        ['min', 'max', 'mean']).transpose())

    # Writing the summary file into a new csv and creating the line chart
    new_data.to_csv(summary_file_name, index=None, header=True)
    plot_creation(new_data)


def plot_creation(new_data):
    # Setting the date column to Date format as we are creating time series chart
    new_data.Date = pd.to_datetime(new_data.Date)
    new_data.set_index('Date', inplace=True)

    # Setting the legends, axis labels
    line_chart = new_data[['Low (EUR)', 'High (EUR)']].plot(
        title='Price range of the last 365 days')
    plot.ylabel('Price in EUR')
    plot.xlabel('Date')
    plot.grid(True)

    # make some gap for the x axis label to be shown properly
    plot.gcf().subplots_adjust(bottom=0.15)

    # exporting the line chart into output file
    line_chart.figure.savefig('price history trend.png')


if __name__ == "__main__":
    main()
