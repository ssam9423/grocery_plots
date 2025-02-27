"""Visualize Data - Creates Graphs showing groceries - Samantha Song - Started 2025.02.26"""
# Create various graphs representing data in groceries.csv

# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import CSV
FILE_NAME = 'groceries.csv'
grocery_list = pd.read_csv(FILE_NAME)
FOLDER = 'Grocery Plots/'

# Histogram - By Food Type
# If food_type is null, replace with other
grocery_list['food_type'] = grocery_list['food_type'].fillna('other')

# Stocked - Unique Food Count
color_count = len(grocery_list[grocery_list['is_stocked']]['food_type'].unique())
stocked_type = sns.countplot(grocery_list[grocery_list['is_stocked']], x='food_type',
                             palette=sns.color_palette('Paired',n_colors=color_count),
                             hue='food_type')
file_name = 'Stocked (Food Type vs Unique Food Count)'
stocked_type.set_title(file_name)
stocked_type.set_xlabel('Food Type')
stocked_type.set_ylabel('Unique Food Count')
# plt.savefig(FOLDER + file_name + '.png', dpi=300)
plt.show()

# Stocked - Show Food Type and Name
color_count = len(grocery_list[grocery_list['is_stocked']]['food'].unique())
stocked_stacked = sns.histplot(data=grocery_list[grocery_list['is_stocked']], x='food_type',
                               weights='stocked_num',
                               palette=sns.color_palette('Spectral',n_colors=color_count),
                               hue='food', multiple="stack")
file_name = 'Stocked (Food Type vs Total Food Count)'
stocked_stacked.set_title(file_name)
stocked_stacked.set_xlabel('Food Type')
stocked_stacked.set_ylabel('Total Food Count')
# plt.savefig(FOLDER + file_name + '.png', dpi=300)
plt.show()

# Need to Buy - Show Food Type
grocery_list['combined_buy_num'] = grocery_list['buy_num'] + grocery_list['add_buy_num']
color_count = len(grocery_list[grocery_list['need_to_buy']]['food_type'].unique())

stocked_stacked = sns.histplot(data=grocery_list[grocery_list['need_to_buy']],
                               x='food_type',
                               weights='combined_buy_num',
                               palette=sns.color_palette('Paired', n_colors=color_count),
                               hue='food_type')
file_name = 'To Buy Food (Types vs Total Food Count)'
stocked_stacked.set_title(file_name)
stocked_stacked.set_xlabel('Food Type')
stocked_stacked.set_ylabel('Total Food Count')
stocked_stacked.locator_params(axis='y', integer=True)
# plt.savefig(FOLDER + file_name + '.png', dpi=300)
plt.show()
