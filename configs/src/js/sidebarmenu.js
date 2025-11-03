/*
Template Name: Admin Template
Author: Wrappixel

File: js
*/
// ==============================================================
// Auto select left navbar
// ==============================================================

//===================
$(function () {
  "use strict";

  // Handle only dropdown toggle links
  document.querySelectorAll("#sidebarnav a.has-arrow").forEach(function (link) {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      e.stopImmediatePropagation(); // ✅ Hard stop duplicate running

      var submenu = this.nextElementSibling;
      var isAlreadyOpen = submenu.classList.contains("in");

      // Close all dropdowns first
      document.querySelectorAll("#sidebarnav ul.in").forEach(function (openMenu) {
        openMenu.classList.remove("in");
      });
      document.querySelectorAll("#sidebarnav a.active").forEach(function (navLink) {
        navLink.classList.remove("active");
      });
      document.querySelectorAll("#sidebarnav li.selected").forEach(function (li) {
        li.classList.remove("selected");
      });

      // Reopen only if it wasn't already open
      if (!isAlreadyOpen) {
        submenu.classList.add("in");
        this.classList.add("active");
        this.closest("li").classList.add("selected");
      }
    });
  });

  // ✅ Handle leaf links separately (no dropdowns)
  document.querySelectorAll("#sidebarnav a:not(.has-arrow)").forEach(function (link) {
    link.addEventListener("click", function (e) {
      // e.stopImmediatePropagation();

      document.querySelectorAll("#sidebarnav a.active").forEach(function (navLink) {
        navLink.classList.remove("active");
      });
      this.classList.add("active");
    });
  });
});
