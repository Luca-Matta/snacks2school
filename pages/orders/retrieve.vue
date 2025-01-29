<template>
  <div>
    <Navbar />
    <div
      class="flex flex-col justify-center items-center text-center gap-2 max-w-44 !py-16 mx-auto"
    >
      <button
        @click="sendOrderFiles"
        class="btn bg-[#a688f9] w-full font-bold uppercase text-xs shadow-button my-4 mb-2 !py-3 !px-6 !rounded-lg"
      >
        Genera file
      </button>
      <button
        @click="retrieveOrderFile('pdf')"
        class="btn bg-black w-full font-bold uppercase text-white text-xs shadow-button my-4 mb-2 !py-3 !px-6 !rounded-lg"
      >
        Scarica PDF
      </button>
      <button
        @click="retrieveOrderFile('csv')"
        class="btn bg-[#ffa500] w-full font-bold uppercase text-xs shadow-button my-4 mb-2 !py-3 !px-6 !rounded-lg"
      >
        Scarica CSV
      </button>
      <button
        @click="generateSnacksLabels"
        class="btn bg-[#bf09bd] text-white w-full font-bold uppercase text-xs shadow-button my-4 mb-2 !py-3 !px-6 !rounded-lg"
      >
        Genera etichette merende
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import axios from "axios";

const getCsrfToken = async () => {
  const response = await axios.get(
    "https://www.snacks2school.com/api/csrf-token/",
    {
      withCredentials: true,
    }
  );
  return response.data.csrfToken;
};

// Call to send the request to generate files
const sendOrderFiles = async () => {
  try {
    const csrfToken = await getCsrfToken();
    const response = await axios.post(
      "https://www.snacks2school.com/api/send-order-files/",
      {},
      {
        headers: {
          "X-CSRFToken": csrfToken,
        },
        withCredentials: true,
      }
    );

    alert("Files generated successfully!");
  } catch (error) {
    console.error("Error generating files:", error);
    alert("Failed to generate files. Please try again.");
  }
};

// Call to retrieve the generated files
const retrieveOrderFile = async (fileType: string) => {
  try {
    const response = await axios.get(
      `https://www.snacks2school.com/api/retrieve-order-file/${fileType}/`,
      {
        responseType: "blob",
        withCredentials: true,
      }
    );

    // Create a URL for the file and trigger a download
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", `order_details.${fileType}`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  } catch (error) {
    console.error(`Error retrieving ${fileType} file:`, error);
    alert(
      `Failed to retrieve ${fileType.toUpperCase()} file. Please try again.`
    );
  }
};

const generateSnacksLabels = async () => {
  try {
    const response = await axios.get(
      "https://www.snacks2school.com/api/snack-order-labels/",
      {
        responseType: "blob",
      }
    );
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", "snack_order_labels.pdf");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  } catch (error) {
    console.error("Error generating labels:", error);
  }
};
</script>