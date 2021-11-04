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



