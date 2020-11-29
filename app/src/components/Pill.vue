<template>
    <div class="w-3/12 flex flex-row space-x-6 p-2 bg-blue-200 rounded-full shadow-md">
        <p class="text-blue-700">{{category}}</p>

        <button class="text-blue-700">X</button>
    </div>
</template>

<script>
export default {
    name: "Pill",
    props: {
        category: String
    }
}
</script>

