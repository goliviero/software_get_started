#include <iostream>
#include <vector>

int main() {

  // Create a vector of integers
  std::vector<int> myVector;

  // Add some elements to the vector
  myVector.push_back(3);
  myVector.push_back(7);
  myVector.push_back(1);

  // Print the elements of the vector
  std::cout << "Elements of the vector: ";
  for (int i = 0; i < myVector.size(); i++) {
    std::cout << myVector[i] << " ";
  }
  std::cout << std::endl;

  // Accessing elements of the vector
  std::cout << "The first element of the vector is: " << myVector[0] << std::endl;

  // Changing an element of the vector
  myVector[1] = 9;

  // Printing the updated vector
  std::cout << "Updated elements of the vector: ";
  for (int i = 0; i < myVector.size(); i++) {
    std::cout << myVector[i] << " ";
  }
  std::cout << std::endl;

  // Removing an element from the vector
  myVector.pop_back();

  // Printing the updated vector
  std::cout << "Elements of the vector after removing the last element: ";
  for (int i = 0; i < myVector.size(); i++) {
    std::cout << myVector[i] << " ";
  }
  std::cout << std::endl;

  // Clearing the vector
  myVector.clear();

  // Printing the updated vector
  std::cout << "Elements of the vector after clearing it: ";
  for (int i = 0; i < myVector.size(); i++) {
    std::cout << myVector[i] << " ";
  }
  std::cout << std::endl;

  return 0;
}
