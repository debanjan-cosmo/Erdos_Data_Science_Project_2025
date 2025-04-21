
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd # added import

sns.set_theme(style="ticks", context="talk", palette="husl", font="sans-serif", font_scale=1.1)


# Function to prettify column names
def prettify_colname(colname):
    if colname.upper() == 'BP_CATEGORY':
        return 'BP Category'
    elif colname.upper() == 'BMI':
        return 'BMI'
    else:
        return colname.replace('_', ' ').title()

#Change ticks fonts
def format_xticklabels(ax):
    labels = []
    for tick in ax.get_xticklabels():
        text = tick.get_text()
        if text.upper() == 'BP_CATEGORY':
            labels.append('BP Category')
        elif text.upper() == 'BMI':
            labels.append('BMI')
        else:
            labels.append(text.upper().replace('_', ' ').title())

    # Get the current tick locations
    locs = ax.get_xticks()
    # Set the new tick locations and labels
    ax.set_xticks(locs, labels)
    ax.set_xticklabels(labels) # set the x tick labels
    
def format_yticklabels(ax):
    labels = []
    for tick in ax.get_xticklabels():
        text = tick.get_text()
        if text.upper() == 'BP_CATEGORY':
            labels.append('BP Category')
        elif text.upper() == 'BMI':
            labels.append('BMI')
        else:
            labels.append(text.upper().replace('_', ' ').title())

    # Get the current tick locations
    locs = ax.get_xticks()
    # Set the new tick locations and labels
    ax.set_xticks(locs, labels)
    ax.set_xticklabels(labels) # set the y tick labels


#Object to remove from list
def remove_objects_from_list(data_list, objects_to_remove):
    """
    Removes all occurrences of specified objects from a list.

    Args:
    data_list: The list from which objects will be removed.
    objects_to_remove: An iterable (like a list, set, or tuple) containing the
                        objects to be removed.
    """
    for item_to_remove in objects_to_remove:
        while item_to_remove in data_list:
            data_list.remove(item_to_remove)

    return data_list

# Format numerical output
def format_sci_notation(val):
    if np.isnan(val):
        return ""
    exponent = int(np.floor(np.log10(abs(val)))) if val != 0 else 0
    base = val / 10**exponent if val != 0 else 0
    return r"${:.2f} \times 10^{{{}}}$".format(base, exponent)


#Format Feature Names
def format_feature_name(feat):
        if feat == "bp_category":
            return "BP Category"
        elif feat == "bmi":
            return "BMI"
        else:
            return feat.replace('_', ' ').title()



