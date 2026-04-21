Cypress.Commands.add("dismissAdsIfPresent", () => {
  cy.get("body").then(($body) => {
    if ($body.find(".fc-dialog-overlay, .fc-consent-root").length > 0) {
      cy.contains("button", "Consent").click({ force: true });
    }
  });
});

Cypress.Commands.add("goToLogin", () => {
  cy.visit("/");
  cy.dismissAdsIfPresent();
  cy.contains("a", "Signup / Login").click({ force: true });
});
