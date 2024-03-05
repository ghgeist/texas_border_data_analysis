#Imports
import pandas as pd
import numpy as np

#Specific a reference dataframe in order to check the data
def extract_reference_df(key, dataframes):
    """
    Extracts a reference dataframe from a dictionary of dataframes.

    Parameters:
    key (str): The key associated with the reference dataframe in the dictionary.
    dataframes_dict (dict): A dictionary where the keys are strings and the values are pandas dataframes.

    Returns:
    tuple: A tuple containing the reference dataframe and the modified dictionary.

    Raises:
    KeyError: If the provided key is not found in the dictionary.
    """
    # Check if the key exists in the dictionary
    if key in dataframes:
        # Extract the dataframe associated with the key and remove the key from the dictionary
        reference_df = dataframes.pop(key)
        # Return both the extracted dataframe and the modified dictionary
        return reference_df, dataframes
    else:
        # Handle the case where the key does not exist
        raise KeyError(f"Key '{key}' not found in the dictionary.")
    
#Check the shapes of the dataframes
def check_shape(reference_df, dataframes_dict):
    """
    Check the shape of each dataframe in the dataframes_dict and compare it with the shape of the reference dataframe.

    Parameters:
    reference_df (pandas.DataFrame): The reference dataframe whose shape will be used for comparison.
    dataframes_dict (dict): A dictionary containing the dataframes to be checked.

    Returns:
    None

    Prints a message for each dataframe whose shape does not match the reference dataframe's shape.
    If all dataframes have the same shape, it prints a message indicating that.

    Example:
    reference_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    dataframes_dict = {'df1': pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}),
                       'df2': pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})}

    check_shape(reference_df, dataframes_dict)
    # Output:
    # df2 shape does not match the reference dataframe.
    # Reference shape: (3, 2), df2 shape: (3, 3)
    """
    # Initialize a list to hold mismatch information
    mismatches = []

    # Iterate over the dictionary items
    for key, df in dataframes_dict.items():
        # Check if the current dataframe's shape matches the reference dataframe's shape
        if df.shape != reference_df.shape:
            # Add the mismatch information to the list
            mismatches.append((key, df.shape))

    # Check if there were any mismatches
    if mismatches:
        # Report all mismatches
        for key, shape in mismatches:
            print(f"{key} shape does not match the reference dataframe.")
            print(f"Reference shape: {reference_df.shape}, {key} shape: {shape}")
    else:
        # If no mismatches were found, print the following message
        print("All dataframes have the same shape.")

#Function to check if all of the columns in the reference dataframe are present in the other dataframes
def check_columns(column_names, dataframes_dict):
    """
    Check if specified columns are present in each dataframe in the given dictionary.

    Args:
        column_names (list): List of column names to check for in the dataframes.
        dataframes_dict (dict): Dictionary containing dataframes to check.

    Returns:
        None

    Prints:
        - If all specified columns are present in all dataframes: 
            "The columns in the old reports are the same as the columns in the reference report"
        - If any dataframe is missing any of the specified columns:
            "Dataframe '{key}' is missing the following columns: {columns}"
    """

    missing_columns = {}  # Dictionary to track dataframes missing any of the specified columns

    for key, df in dataframes_dict.items():
        # Check if all specified columns are present in the dataframe
        missing = [column for column in column_names if column not in df.columns]
        if missing:
            missing_columns[key] = missing

    if not missing_columns:
        print("The columns in the old reports are the same as the columns in the reference report")
    else:
        for key, columns in missing_columns.items():
            print(f"Dataframe '{key}' is missing the following columns: {columns}")

def check_column_values(column_name, reference_df, dataframes_dict):
    """
    Compare the values of a specific column across multiple dataframes with a reference dataframe.

    Parameters:
    column_name (str): The name of the column to compare.
    reference_df (pandas.DataFrame): The reference dataframe containing the column values to compare against.
    dataframes_dict (dict): A dictionary of dataframes to compare against the reference dataframe.

    Returns:
    pandas.DataFrame: A summary dataframe showing the missing column values in each dataframe compared to the reference dataframe.
    """
    
    # Get the set of unique values from the reference dataframe, treating NaN as a distinct value
    reference_values = set(reference_df[column_name].dropna().unique())
    reference_values.add(np.nan) if reference_df[column_name].isnull().any() else reference_values
    
    # Initialize a dictionary to store comparison results
    results = {'reference': sorted(reference_values)}
    
    for key, df in dataframes_dict.items():
        # Ensure the column exists in the dataframe
        if column_name not in df.columns:
            print(f"{key} dataframe does not have the column '{column_name}'.")
            continue
        
        # Check data type consistency
        if df[column_name].dtype != reference_df[column_name].dtype:
            print(f"Data type mismatch in '{key}' for column '{column_name}': "
                  f"{df[column_name].dtype} vs {reference_df[column_name].dtype}")
            continue
        
        # Get the set of unique values from the current dataframe, treating NaN distinctly
        df_values = set(df[column_name].dropna().unique())
        df_values.add(np.nan) if df[column_name].isnull().any() else df_values
        
        # Compare the sets of values
        missing_values = reference_values - df_values
        if missing_values:
            results[key] = sorted(df_values)
            print(f"'{key}' dataframe is missing the following column values: {sorted(missing_values)}")
        else:
            print(f"Column values in the reference dataframe match the values in the '{key}' dataframe.")
    
    # Create a summary dataframe
    summary_df = pd.DataFrame(dict([(k, pd.Series(list(v))) for k, v in results.items()]))
    return summary_df