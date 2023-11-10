<!--

  <script>
  function validate() {
    return {
      full_name: document.getElementById("id_full_name").value,
      email: document.getElementById("id_email").value,
      comment: document.getElementById("id_comment").value,
    };
  }

  const form = document.getElementById("add-comment");
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    fetch("{{post.get_comment_upload_url}}", {
      method: "POST",
      headers: { "X-CSRFToken": "{{csrf_token}}" },
      mode: "same-origin",
      body: validate(),
    })
      .then((response) => response.json())
      .then((data) => {
        alert("Your comment was posted successfully");
      })
      .catch((error) => {
        alert("Something went wrong. Try again");
      });
  });
</script>
-->
