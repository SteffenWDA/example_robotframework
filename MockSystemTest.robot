*** Settings ***
Documentation    Suite description
Library  MockTestDataInsertion.py
Library  MockTestDataProcessing.py
Library  MockUseCaseAssertions.py
Resource  MockKeywordUsage.robot

*** Test Cases ***
Verfiy creation of lead conversion table
  post snow plow events
  trigger segment processing  cadia-stands-1640  grnry-belt-15  devops
  trigger data transfer job  export_job
  Pull data processed by uniserv
  trigger segment processing  cadia-stands-1641  grnry-belt-15  devops
  verify content of example segment







