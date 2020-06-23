
//let calls = 0
function solution(elevationList){
  //calls = 0
  if (!elevationList || elevationList.length < 3){
    // invalid input
    return 0
  }
  return waterLevel(elevationList, elevationList[1], 0, 2, elevationList[0])
}

function waterLevel(elevationList, currentHeight, leftBoundryIndex, rightBoundryIndex, leftMax){
  //calls++
  if (rightBoundryIndex >= elevationList.length){
    // If out of bounds on the right then we are done calculating
    return 0
  }
  leftHeight = elevationList[leftBoundryIndex]
  rightHeight = elevationList[rightBoundryIndex]

  if ( leftHeight > leftMax ){
    leftMax = leftHeight
  }
  /* For debugging purposes only */
  // console.log(`H: ${currentHeight}`)
  // console.log(`RH: ${rightHeight}`)
  // console.log(`LH: ${leftHeight}`)
  // console.log(`LM: ${leftMax}`)
  // console.log()
  if ( leftHeight < currentHeight && currentHeight >= leftMax){
    // If left boundry doesn't hold water reset starting point to the right
    return 0 + waterLevel(elevationList, rightHeight, rightBoundryIndex-1, rightBoundryIndex+1, leftMax)
  }
  if ( rightHeight < currentHeight ){
    // If elevation is downhill to the right reset reference point to the right
    return 0 + waterLevel(elevationList, rightHeight, rightBoundryIndex-1, rightBoundryIndex+1, leftMax)
  }
  if ( rightHeight >= currentHeight && leftHeight >= currentHeight ){
    // if we are in a valley start counting things
    if(rightHeight === leftHeight){
      // local minimum: count valley and keep seeking right
      return countVolumeContinueSeeking(elevationList, rightHeight, currentHeight, leftBoundryIndex, rightBoundryIndex, leftMax)
    }
    if ( leftHeight > rightHeight ){
      // count the diff between right and current level and keep seeking right
      return countVolumeContinueSeeking(elevationList, rightHeight, currentHeight, leftBoundryIndex, rightBoundryIndex, leftMax)
    }
    if (rightHeight > leftHeight){
      // count diff between left and current level and either seek left or reset reference point to the right
      return countVolumeContinueSeeking(elevationList, leftHeight, currentHeight, leftBoundryIndex, rightBoundryIndex, leftMax)
    }
  }
  console.log('WTF')
  throw Error(` rightHeight: ${rightHeight} leftHeight: ${leftHeight} currentHeight: ${currentHeight} leftMax: ${leftMax}`)
}

function countVolumeContinueSeeking(elevationList, boundryHeight, currentHeight, leftBoundryIndex, rightBoundryIndex, leftMax){
  // get the difference between the current counted height and the boundry provided
  additionalHeight = boundryHeight - currentHeight
  // calculate the additional volume to add
  addedVolume = additionalHeight * (rightBoundryIndex - leftBoundryIndex - 1)
  if(boundryHeight == elevationList[rightBoundryIndex]){
    // if the boundry is a right boundry add volume and keep seeking right
    return addedVolume + waterLevel(elevationList, additionalHeight + currentHeight, leftBoundryIndex, rightBoundryIndex + 1, leftMax)
  }else if(leftHeight < leftMax){
    // if the left boundry is not the highest point currently seen add volume and seek left
    return addedVolume + waterLevel(elevationList, additionalHeight + currentHeight, leftBoundryIndex - 1, rightBoundryIndex, leftMax)
  } else{
    // if the boundry is the highest point currently seen then add volume and reset reference to the right
    return addedVolume + waterLevel(elevationList, elevationList[rightBoundryIndex], rightBoundryIndex - 1, rightBoundryIndex + 1, leftMax)
  }
}

TEST_CASES = [
  {input: [0,0,0,0,0],expected:0},
  {input: [0,1,0],expected:0},
  {input: [0,1,0,1,0],expected:1},
  {input: [3,2,1,2,3],expected:4},
  {input: [1,2,3,2,1], expected: 0},
  {input: [0,1,0,2,1,0,1,3,2,1,2,1], expected: 6},
  {input: [4, 0, 1, 5, 0, 5, 3, 2, 4, 1], expected: 15},
  {input: [4, 3, 6, 1, 0, 5], expected: 10},
  {input: [1, 1, 1, 0, 0, 1], expected: 2},
]

TEST_CASES.forEach(({input, expected},index) => {
  result = solution(input)
  if(result != expected){
    console.log(`Test ${index} failed. ${result} != ${expected}`)
  }else{
    console.log(true)
  }
  //console.log(calls)
});
