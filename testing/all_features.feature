# 1st Scenario
Feature: Sign up for an account on the Q&A site

User Story: As a user, I would like to sign up for an account to be able to post questions.

Scenario: As a user I want to be able to fill out a form to create an account
  Given I am on any page
  When I click on the "Sign up" link
  Then I should be on the "Sign up" page
  And I should see the form fields to sign up
  When I fill out the required fields
  Then I should be able to create an account
  When I click on create account
  Then I should see my profile page
  
#2nd Scenario
Feature: Post a new question
  
User Story: As a user, I would like to create a new question then have it published to the forum for people to answer
  
Scenario: As a user I would like to be able to post a question as soon as I sign on
  Given I am on the home page 
  When I click on "Posts new Question"
  Then I should be on the "Posts" page
  And I should see enter question field
  When I fill out the new question field
  Then I should click post question button
  When I click the post question button
  Then my question should be posted to the forum

# 3rd Scenario

Feature: Browse through posts

User Story: As a user I would like to browse through different posts about topics of my interest.

Scenario: As a user I would like to be able to search for a topic and view posts other people have posted on that same topic.
  Given I am on the home page
  When I click the search bar
  Then I type what subject I would like to search
  And I click the enter key 
  Then I see a list of posts that are relevant to the topic I wrote.
  And I can scroll through all the different posts
  Then I can select whichever one I am most interested in and see the entire post
  
# 4th Scenario

Feature: Edit an existing post/question

User Story: As a user, I want to be able to go back to a post/question I’ve published and be able to edit it.

Scenario:
  Given I am on the home page
  When I click on the “Profile” link
  Then I should be on the “My profile” page
  When I click on the “My notes” link
  Then I should be on the “My Notes” page
  When I click on the “Edit” link on an existing question/post
  Then I should be on the “Note [id]” page
  And I should see the “Subject” field with already existing subject
  And I should see the “Text” field with already existing text
  When I click on the “Update” link
  Then I should be able to see the question, but updated with added content



