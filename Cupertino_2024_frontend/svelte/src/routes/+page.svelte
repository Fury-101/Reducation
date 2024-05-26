<script>
	import Header from "./Header.svelte";
	let query='';
	function onSubmit(e) {
		setTimeout(()=>window.location=`/course/${query}`, 10000);
		// window.location = `/course/${query}`
  	}
</script>

<div class='z-10 absolute'>
	<Header></Header>
</div>

<div class='flex flex-col justify-end items-center h-screen w-screen absolute overflow-hidden'>
	<form on:submit|preventDefault={onSubmit} class='w-3/4'>
		<input type='text' bind:value={query} class='bg-gray-900 opacity-80 text-white/60 text-xl p-4 font-normal mb-12 ml-10 mr-10 rounded-xl w-full' placeholder="Calculus">
	</form>
</div>

<div class='flex flex-col items-center justify-center h-screen overflow-hidden'>
	<div class='blob absolute'></div>
	<h class='opacity-87 font-medium text-white text-center text-7xl absolute'>What would you like to learn about?</h>
</div>


<style>
:global(body) {
    background-color: #2e2e2e;
}
</style>