$(document).ready(function () {
  $("#tutorial").on("click", function () {
    Swal.fire({
      html: `<iframe width="1120" height="630" src="https://www.youtube.com/embed/RH6DsyZWKjE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`,
      width: 1190,
      showConfirmButton: false,
      showCloseButton: true,
    });
  });
});
