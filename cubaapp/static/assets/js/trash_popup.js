document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".trash-3").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      const form = btn.closest("form");

      if (!form) {
        console.error("No form found for trash button");
        return;
      }

      Swal.fire({
        title: "Are you sure?",
        text: "Do you really want to delete this upload?",
        showCancelButton: true,
        confirmButtonColor: "#16C7F9",
        cancelButtonColor: "#FC4438",
        confirmButtonText: "Yes, delete it!",
        imageUrl: "/static/assets/images/gif/trash.gif",
        imageWidth: 120,
        imageHeight: 120,
      }).then((result) => {
        if (result.isConfirmed) {
          form.submit();
        }
      });
    });
  });
});
