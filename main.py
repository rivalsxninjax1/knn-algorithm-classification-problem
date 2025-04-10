import math
import csv
from collections import Counter

def load_dataset(file_path):
    dataset = []
    try:
        with open(file_path, mode='r', newline='') as csvfile:
          reader = csv.DictReader(csvfile)
          for row in reader:
             weight = float(row['weight'])
             texture_score = float(row['texture_score'])
             label = row['label']
             dataset.append((weight, texture_score, label))
    except FileNotFoundError:
       print(f"file '{file_path}' not found.")
    return dataset

def euclidean_distance(point1, point2):
   """calculating the euclidean distance betweenthe two  points"""
   return math.sqrt((point1[0]-point2[0])**2 +(point1[1]-point2[1])**2)

def knn_classify(new_point, dataset, k=3):
   """classify a new point using the knn algorithm.
   
   parameters:
      new_point(tuple): the features ofthe new point (e.g. (160,7)).
      datset (list):
      list of the tupple where each tuple is (weight, texture_score, label)
      l(int):nukber of nearest neighbours to consider 
      returns 
      str: the predicted label
      """
   
   # calculating the distance from new point to each poitn in the dataset 
   distances= []

   for data in dataset:
      features = (data[0], data[1])
      distance = euclidean_distance(new_point, features)
      distances.append((distance, data[2]))

    #sorting the distance and selecting the nearest neighbours
   distances.sort(key=lambda x : x[0])
   k_nearest = distances[:k]

   #extracting the labels from the k nearest neighbours
   labels = [label for _, label in k_nearest]
   #return the most common label (majority vote)
   return Counter(labels).most_common(1)[0][0]
if __name__ == "__main__":
   dataset = load_dataset('src/data.csv')
   #loading the datafile frrom the csv file 
   if not dataset:
      exit("dataset could nothbe found ")

new_fruit = (160, 7)
k =  3 #number of neighbours to consider
#classify the new fruit 
predicted_label = knn_classify(new_fruit, dataset,k)
print(f"the new fruit with features  {new_fruit} is classified as: {predicted_label}")
