import { Given, When, Then } from "@badeball/cypress-cucumber-preprocessor";

Given("que acesso a home da Automation Exercise", () => {
  cy.visit("/");
  cy.dismissAdsIfPresent();
  cy.contains("AutomationExercise").should("be.visible");
});

When("eu vou para login", () => {
  cy.contains("a", "Signup / Login").click({ force: true });
  cy.url().should("include", "/login");
});

When("faco login com credenciais validas", () => {
  const email = Cypress.env("AE_EMAIL") || "teste.aluno@example.com";
  const password = Cypress.env("AE_PASSWORD") || "123456";

  cy.get("input[data-qa='login-email']").type(email);
  cy.get("input[data-qa='login-password']").type(password);
  cy.get("button[data-qa='login-button']").click();
});

When("adiciono o primeiro produto ao carrinho", () => {
  cy.contains("a", "Products").click({ force: true });
  cy.url().should("include", "/products");
  cy.get(".product-image-wrapper .single-products").first().trigger("mouseover");
  cy.get(".product-overlay .add-to-cart").first().click({ force: true });
  cy.contains("button", "Continue Shopping").click({ force: true });
});

When("acesso o carrinho", () => {
  cy.contains("a", "Cart").click({ force: true });
  cy.url().should("include", "/view_cart");
});

Then("devo visualizar o produto no carrinho", () => {
  cy.get(".cart_info").should("be.visible");
  cy.get(".cart_description").its("length").should("be.greaterThan", 0);
});

When("eu clico em Proceed To Checkout", () => {
  cy.contains("a", "Proceed To Checkout").click({ force: true });
});

Then("devo visualizar a tela de checkout", () => {
  cy.url().should("include", "/checkout");
  cy.contains("Address Details").should("be.visible");
});
