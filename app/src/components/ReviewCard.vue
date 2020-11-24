<template>
<div class="container max-w-xs box-border p-4 border-2">
    <div><p>{{reviewText}}</p></div>
    <div class="text-right"><p>{{user}}</p></div>
</div>
</template>

<script>
export default {
    data(){
        return {
            user: "- A random user",
            reviewText: "In aliquip labore amet minim dolor eiusmod voluptate. Exercitation aute quis consectetur veniam culpa laboris anim culpa et mollit officia. "
        }
    }
}
</script>